import inspect
import structlog

logger = structlog.get_logger(__name__)


class ExternalServiceTimeoutError(Exception):
    """Custom exception for external service timeouts."""
    pass


def pretty_request(request):
    """Helper function to extract and format request details for logging."""
    request_info = {}
    if request:
        request_info.update(
            method=request.method,
            path=request.path,
            headers=dict(request.headers),
            user=str(request.user),
            remote_addr=request.META.get("REMOTE_ADDR"),
        )
        data = getattr(request, 'data', None)
        if data is None:
            try:
                data = request.body.decode(errors="replace")
                request_info['body'] = data
            except Exception:
                pass
        elif data:
            request_info['data'] = data
    return request_info


def log_api_call(func):
    """Decorator to log API calls with request and response details."""
    is_async = inspect.iscoroutinefunction(func)
    if is_async:
        async def wrapper(*args, **kwargs):
            request = args[1] if len(args) > 1 else None
            request_info = pretty_request(request)
            response = await func(*args, **kwargs)
            logger.info({'endpoint': func.__name__, 'request': request_info, 'response': response.data})
            return response
    else:
        def wrapper(*args, **kwargs):
            request = args[1] if len(args) > 1 else None
            request_info = pretty_request(request)
            response = func(*args, **kwargs)
            logger.info({'endpoint': func.__name__, 'request': request_info, 'response': response.data})
            return response
    return wrapper


def log_api_viewset(wrapper):
    """Wrapper to apply log_api_call to all viewset CRUD methods."""
    def decorate_viewset(cls):
        for name in ('list', 'retrieve', 'create', 'update', 'partial_update', 'destroy'):
            if hasattr(cls, name):
                original_method = getattr(cls, name)
                setattr(cls, name, wrapper(original_method))
        return cls
    return decorate_viewset
