# Foxy

Foxy is a proxy server that lets you access Font Awesome's private Python package index without exposing your Font
Awesome package manager token in your project's source code.

## Why?

If you have a Font Awesome Pro license, you can install Font Awesome Pro's Python package from the index at
`https://dl.fontawesome.com/{FONTAWESOME_TOKEN}/fontawesome-pro/python/simple`, where `{FONTAWESOME_TOKEN}` is your
Font Awesome package manager token. Unfortunately, putting this URL in any file you'd want to check into source control
— like a `requirements.txt` or a `pyproject.toml` — will make it difficult for you to make your source code publicly
available without exposing your token to the world.

Foxy solves this problem by taking your token via HTTP Basic authentication and returning a redirect to Font Awesome's
package index.

## Usage

Using the faculties provided by your favorite Python package manager, add `https://foxy.celsiusnarhwal.dev/simple` as a package index. For
credentials, the username can be whatever you want, and the password must be your Font Awesome package manager token.

Here's an example using [Poetry](https://python-poetry.org/):

```toml
# pyproject.toml
[[tool.poetry.source]]
name = "fontawesome"
url = "https://foxy.celsiusnarhwal.dev/simple"
secondary = true

```

```bash
poetry config http-basic.fontawesome celsiusnarhwal ${FONTAWESOME_TOKEN}
```

## Security

Foxy never stores or logs your token; it uses it to form the index URL and then throws it away. You don't have to take
my word for it because you can just look at the source code. If you're _really_ paranoid, you can even deploy your own
instance of Foxy by clicking the button below.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=github.com%2Fcelsiusnarhwal%2Ffoxy&project-name=foxy&repository-name=foxy)

## License

Foxy is licensed under the [MIT License](LICENSE.md).
