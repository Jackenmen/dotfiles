# don't put duplicate lines or lines starting with space in the history.
setopt HIST_IGNORE_DUPS
setopt HIST_IGNORE_SPACE

# add timestamps
setopt EXTENDED_HISTORY

# append to the history file (immediately, not on shell exit), don't overwrite it
setopt INC_APPEND_HISTORY

HISTFILE=~/.zsh_history
HISTSIZE=10000
SAVEHIST=100000
