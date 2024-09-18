from flask import jsonify, make_response

'''def Rs(data=None):
    res = {
        'code': 200,
        'message': 'success',
        'data': data
    }
    return jsonify(res)


def R_with_args(code, message, data=None):
    res = {
        'code': code,
        'message': message,
        'data': data
    }
    return jsonify(res)'''


def jsonify_with_args(data, code=200, *args):
    '''

    :param data:
    :param code:
    :param args:
    :return:
    '''
    assert isinstance(data, dict)
    return make_response(jsonify(data), code, *args)
