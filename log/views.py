from django.http import HttpResponse
def logo(request):
    OPENID_LOGO_BASE_64 = """
    R0lGODlhEAAQAMQAAO3t7eHh4srKyvz8/P5pDP9rENLS0v/28P/17tXV1dHEvPDw8M3Nzfn5+d3d
    3f5jA97Syvnv6MfLzcfHx/1mCPx4Kc/S1Pf189C+tP+xgv/k1N3OxfHy9NLV1/39/f///yH5BAAA
    AAAALAAAAAAQABAAAAVq4CeOZGme6KhlSDoexdO6H0IUR+otwUYRkMDCUwIYJhLFTyGZJACAwQcg
    EAQ4kVuEE2AIGAOPQQAQwXCfS8KQGAwMjIYIUSi03B7iJ+AcnmclHg4TAh0QDzIpCw4WGBUZeikD
    Fzk0lpcjIQA7
    """
    return HttpResponse(
        OPENID_LOGO_BASE_64.decode('base64'), mimetype='image/gif'
    )
# Logo from http://openid.net/login-bg.gif
# Embedded here for convenience; you should serve this as a static file