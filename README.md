# جنگو رست فریمورک و ساخت RESTapi 

### تکنولوژی ها:

- پایتون
- جنگو
- virtualbox
- vagrant
- vscode

توی این پروژه ابتدا محیط کاری یا ورک اسپیس خودمون رو ایجاد میکنیم سیستم عامل من ubuntu 24 LTS هستش و ابزار هامون رو نصب میکنیم

بعد از نصب اقدام به کلون کردن پروژه از گیتهاب و ایجاد فایل های مرسوم `gitignore` `license` و `README` میشویم

سپس با استفاده از دستور `vagrant init SERVERNANE` اقدام به ایجاد فایل کانفیگ محیط کانتینری vagrant میکنیم تا سرورمجازی لوکالمون رو ایجاد کنیم

سپس با تغییرات مناسب فایل ایجاد شده `Vagrantfile` کانفیگ هارو ست میکنیم و با دستور `vagrant up` سرور رو اجرا و بیلد میکنیم و درنهایت به صورت ssh و با دستور `vagrant ssh` وارد سرور خودمون میشیم


install virtualbox -> vagrant -> setup git and github

#### config and setup vagrant server (virtaulbox)
- vagrant for build just type command `vagrant init OSNAME`
- vagrant create a config file `Vagrantfile`
- and just modify this file and create own box
- command of run server just type command `vagrant up`
- and ssh to local server of vagrant just type `vagrant ssh`


after run ssh server in vagrant just `cd /vagrant`
this dir sincronize for main diractory mean just create a one file this file create to `RESTapi` document

that means just remove a file at main dir this file atoumatic removed from `/vagrant` dir {virtaul ssh server}

```bash
cd /Vagrant
```