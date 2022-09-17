Как как добавить ключ в ssh-agent и склонировать репозиторий:
1) git config --global user.name "German-Nazarov"
2) git config --global user.email "gooditsn@mail.ru"
3) eval "$(ssh-agent -s)"
4) ssh-add ~/.ssh/id_ed25519
5) ssh -T git@github.com -> yes
6) git clone git@github.com:German-Nazarov/NazarovRepo.git

