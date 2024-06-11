import plt_inc


def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in plt_inc.ALLOWED_EXTENSIONS

def get_dot_file(filename):
  return filename.rsplit('.', 1)[1].lower()
