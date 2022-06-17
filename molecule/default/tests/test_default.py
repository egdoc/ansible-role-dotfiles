import os
import pytest
import testinfra.utils.ansible_runner

DOTFILES_REPOSITORY = os.path.expanduser('~/.config/dotfiles')
DOTFILES_LINKED = [
    '~/.vimrc',
    '~/.vim',
    '~/.gvimrc',
    '~/.bash_aliases',
    '~/.bash_profile',
    '~/.bashrc',
    '~/.lftprc',
    '~/.npmrc',
    '~/.pylintrc',
    '~/.config/dconf'
]

def test_repository_exists(host):
    assert host.file(DOTFILES_REPOSITORY).is_directory


@pytest.mark.parametrize('link', DOTFILES_LINKED)
def test_symlink_exists(host, link):
    link = os.path.expanduser(link)
    target = os.path.join(DOTFILES_REPOSITORY, link.split('/')[-1].strip('.'))
    assert host.file(link).linked_to == target
