# SSH pub keys for Rancher Labs

Text database of Rancher Labs public ssh keys.

# Goals
* avoid the use of shared SSH keys (for instance in CI environments)
* make it easy to populate a node with required set of keys from the command-line (curl, wget, httpie, etc)
* make the repo layout flexible enough to simulate "groups" for different use-cases.

# Usage

Use your favorite HTTP client to pull down a set of public SSH keys. The repo is organized
such that you can simulate user groups via filesystem hierarchy.

For instance, to download the pub key for user 'nrvale0' using [HTTPie](http://httpie.org):

```ShellSession
➜  ~ http https://raw.githubusercontent.com/rancherlabs/ssh-pub-keys/master/ssh-pub-keys/users/nrvale0
HTTP/1.1 200 OK
Accept-Ranges: bytes
Access-Control-Allow-Origin: *
Cache-Control: max-age=300
Connection: keep-alive
Content-Encoding: gzip
Content-Length: 351
Content-Security-Policy: default-src 'none'; style-src 'unsafe-inline'
Content-Type: text/plain; charset=utf-8
Date: Fri, 14 Oct 2016 21:10:51 GMT
ETag: "c0b7df204c2da83a5c0154c6562593a1047566f4"
Expires: Fri, 14 Oct 2016 21:15:51 GMT
Source-Age: 56
Strict-Transport-Security: max-age=31536000
Vary: Authorization,Accept-Encoding
Via: 1.1 varnish
X-Cache: HIT
X-Cache-Hits: 1
X-Content-Type-Options: nosniff
X-Fastly-Request-ID: 5390580b4919dbc5691a1ab7af6040bf8d1526fe
X-Frame-Options: deny
X-Geo-Block-List:
X-GitHub-Request-Id: 689C5B1B:48FF:45E74F2:580149A3
X-Served-By: cache-lax8635-LAX
X-XSS-Protection: 1; mode=block

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDFGjXK1nKnGIIg7LERaDkBegCGFrTHgZ0d81f3kzifRINj2UjV9I5kWAMO9M3USfN0iwy/GFn95obmDj3M5gH+1/U8pP3UtP/J6XTrEcwiv63sSS+i1ib3cDeswoqTqDUbu89PncyfRCobkUHrXJWzY/5CEfXtDkBqCPMTQuV3sL+lueWHP1yV2HYSlpq/R+aS8y6DBx4lTRlkOODSRdmkWQg23HfpcWR3uzUeu5wcmVFEpjRbFwVwhLtARCYGVb5dPs65WbD+g6j47fpXjYcSTdSqa29QC5iQJDHOhcgnCVLlxybRLZA8nAtFgQyrFXRVYy2IDUStfo6KoreMkNT1 nrvale0
```

# Adding a pub key

* Fork the repo.
* Add your key to the appropriate files in the hierarchy
* Optionally, do a local test run:

```ShellSession
➜ ~ dapper ./scripts/ci
```
Of course this implies the presence of [Dapper](https://github.com/rancher/dapper) - the Docker Build Wrapper.

* If the test fails, fix your additions. ;)
* Send in a Pull Request.

# Contributors
* Nathan Valentine - nathan@rancher.com | nrvale0@gmail.com | @nrvale0

# Support / PRs / Issues

[https://github.com/rancherlabs/ssh-pub-keys](https://github.com/rancherlabs/ssh-pub-keys)
