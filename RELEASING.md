# Release process

Signing key: B993FF98A90C9AB1 (https://bargen.dev/B993FF98A90C9AB1.txt)

Used variables:

    export VERSION={VERSION}
    export GPG=B993FF98A90C9AB1

Update version numbers:

    vim -p setup.py CHANGELOG.md RPLCD/__init__.py docs/conf.py

Do a signed commit and signed tag of the release:

    git add setup.py CHANGELOG.md RPLCD/__init__.py docs/conf.py
    git commit -S${GPG} -m "Release v${VERSION}"
    git tag -u ${GPG} -m "Release v${VERSION}" v${VERSION}

Build source and binary distributions:

    python3 setup.py sdist
    python3 setup.py bdist_wheel

Sign files:

    gpg --detach-sign -u ${GPG} -a dist/RPLCD-${VERSION}.tar.gz
    gpg --detach-sign -u ${GPG} -a dist/RPLCD-${VERSION}-py3-none-any.whl

Upload package to PyPI:

    twine3 upload dist/RPLCD-${VERSION}*
    git push
    git push --tags
