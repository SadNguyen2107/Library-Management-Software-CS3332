from src.main import bp

@bp.route('/')
def index():
    return 'This is the main Blueprint'