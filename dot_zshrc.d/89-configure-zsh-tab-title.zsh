export ZSH_TAB_TITLE_ENABLE_FULL_COMMAND=true
export ZSH_TAB_TITLE_DEFAULT_DISABLE_PREFIX=true
if [ "$TERM" != xterm-kitty ]; then
    export SHELDON_PROFILE=not-kitty
fi
