from flask import jsonify, make_response


def jsonify_with_args(data, code=200, *args):
    """
    :param data:
    :param code:
    :param args:
    :return:
    """
    assert isinstance(data, dict)
    return make_response(jsonify(data), code, *args)
