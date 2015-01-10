from flask import Flask, request, make_response
import hmac, subprocess, os
from hashlib import sha1

app = Flask(__name__)
app.debug = False

ip, port = "0.0.0.0", 8080
deploy_path = "/var/public_html"
source_path = "/var/local_git_repo/jekyll_source"
github_secret = "webhook_secret"

@app.route("/push", methods=["POST"])
def build_blog():

    sign = request.headers.get("X-Hub-Signature")
    if not sign:
        return make_response("Bad Request", 400)

    sha_name, key = sign.split("=")

    if "sha1" != sha_name:
        return make_response("Unknown algorithm", 406)

    computed_hash = hmac.new(github_secret, msg=request.data, digestmod=sha1)
    if computed_hash.hexdigest() != key:
        return make_response("Signatures don't match", 401)

    try:
        os.chdir(source_path)
        os.system("git pull origin master")
        subprocess.Popen(["jekyll", "build", "-s", source_path, "-d", deploy_path])
    except Exception as e:
        return make_response("Error: %s" % (e.message), 500)

    return make_response("ok", 200)


if __name__ == "__main__":
    app.run(ip, port)

