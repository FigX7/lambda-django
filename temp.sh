#!/bin/sh
alias zappashell3='docker run -ti --env-file ./.env -v "$(pwd):/var/task" -v ~/.aws/:/root/.aws --rm myzappa'
alias zappashell3 >> ~/.bash_profiles
