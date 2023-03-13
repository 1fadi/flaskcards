# custom filters for jinja's templates


def ifchanged(value, oldvalue):
    if value != oldvalue:
        result = value
    else:
        result = ""
    return result
