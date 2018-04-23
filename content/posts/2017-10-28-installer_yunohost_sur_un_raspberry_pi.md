Title: Installer YunoHost sur un Raspberry Pi
Date: 2017-10-28
Category: Blog
Tags: yunohost, autohebergement
Slug: installer_yunohost_sur_un_raspberry_pi
cover: https://framagit.org/Rafi594/pelican/raw/master/images/etcher.png



Dans cet article nous allons installer YunoHost sur un Raspberry Pi
Prérequis

*    Un Raspberry Pi 0, 1, 2 ou 3 ;
*    Une carte SD : au moins 8 Go et Classe 10
*    Un adaptateur secteur pour la alimenter la carte
*    Un câble ethernet/RJ-45 pour brancher la carte à votre routeur/box internet. Avec le Raspberry Pi Zero vous pouvez connecter votre carte avec un câble OTG et un adaptateur Wifi USB.

Téléchargement de l’image pour Raspberry Pi

Rendez vous sur https://build.yunohost.org et choisissez Raspberry Pi et cliquez sur image et sha256 pour télécharger les fichiers nécessaires.

Ensuite dézippez le fichier obtenu dans un dossier et copiez le deuxième fichier qui se termine en .sum dedans.
Installation de Etcher

Ensuite rendez vous sur https://etcher.io pour installer etcher qui permet de copier une image disque sur une carte sd

Sélectionnez l’image qui se trouve dans le dossier précédemment crée, choisissez votre carte sd et faites Flash
![](https://rafi59.codelib.re/blog/wp-content/uploads/2017/08/etcher.png)
Quand la copie est terminée mettez la carte sd dans votre Raspberry Pi et démarrez le en branchant l’alimentation.
Postinstallation

Pour démarrer la postinstallation regardez dans les paramètres de votre routeur pour trouver l’adresse ip de votre Raspberry Pi

 

Connectez vous à l’adresse ip de votre Raspberry Pi et normalement vous allez tomber sur cette page

 ![](https://rafi59.codelib.re/blog/wp-content/uploads/2017/08/postinstall_web.png)

Sur la page suivante vous allez choisir un domaine :

*    Si vous avez votre domaine que vous avez acheté choisissez la première option
*    Si vous n’avez pas de nom de domaine choisissez la deuxième option qui vous permettra d’avoir un sous domaine gratuit en .nohost.me ou .noho.st

Dans la prochaine étape vous allez choisir un mot de passe d’administration

Et vous avez un serveur YunoHost tout neuf dans le prochain article nous allons installer des applications essentielles.
