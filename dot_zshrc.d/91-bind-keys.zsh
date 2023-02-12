# add shell-word movement/deletion bindings
bindkey '^[[1;5C' forward-word
bindkey '^[[1;5D' backward-word
bindkey '^H' backward-kill-word
bindkey '^[[3;5~' kill-word

# add subword movement/deletion bindings
bindkey '^[[1;3C' forward-subword
bindkey '^[[1;3D' backward-subword
bindkey '^[^?' backward-kill-subword
bindkey '^[[3;3~' kill-subword
