# don't put duplicate lines or lines starting with space in the history.
setopt HIST_IGNORE_DUPS
setopt HIST_IGNORE_SPACE

# append to the history file, don't overwrite it
setopt APPEND_HISTORY

HISTFILE=~/.bash_history
HISTSIZE=10000
SAVEHIST=100000
