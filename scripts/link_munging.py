import re


# Useful for testing:
#   https://regex101.com
#   https://regexr.com


def convert_github_url(v1):
    # https://github.com/isiahmeadows/github-limits
    optional_github_prefix = r'(GitHub - ){0,1}'
    user_name = r'([A-Za-z-\d)]+)'
    repo_name = r'([a-z\d\-_.]+)'
    description = r'(: [^\]]+){0,1}'
    github_url = fr'https://github.com/{user_name}/{repo_name}/?'

    whole_pattern = fr"""\[{optional_github_prefix}{user_name}/{repo_name}{description}\]\({github_url}\)"""
    print(f"python:     {whole_pattern}")

    js_pattern = whole_pattern.replace('/', r'\/')
    print(f"javascript: {js_pattern}")

    github_repo_hyperlink = re.compile(whole_pattern)

    # [$2/**$3**](https://github.com/$2/$3)$4 on PyCharm
    return github_repo_hyperlink.sub(r'[\2/**\3**](https://github.com/\2/\3)\4', v1)
