import pkg_resources


packagenames = ["DateTime","Flask","importlib-metadata","itsdangerous","Jinja2","jsonify",
                "MarkupSafe","Werkzeug","zipp","DateTime","click"]

for item in packagenames:
    print(item, " == ", pkg_resources.get_distribution(item).version)


