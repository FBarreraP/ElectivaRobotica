<h1>Aula 2</h1>

En esta clase ...

<h2>Repositorio git</h2>

Instalar git en Windows, a través del siguiente link: https://git-scm.com/downloads

Los repositorios GitHub y GitLab son utilizados principalmente por el terminal, donde los comandos son similares a los de Linux, algunos de dichos comandos son:

```linux
COMANDOS LINUX
ls -> Muestra la lista de archivos en la ruta actual
la -a -> Muestra la lista de archivos incluyendo archivos ocultos en la ruta actual
pwd -> Muestra la ruta actual
cd [FOLDERNAME] -> Entra a una carpeta especificada
cd .. -> Regresa al punto anterior de la ruta
cp [FILETOCOPY] [DESTINATIONFOLDER]-> Copia archivos o carpetas
mv [FILETOMOVE] [DESTINATIONFOLDER]-> Mueve archivos y carpetas
mv [ORIGINALFILE] [RENAMEDFILE]-> Renombra archivos y carpetas
touch [FILE] -> Crea un archivo en la ruta actual
rm [FILE] -> Elimina un archivo
rm -r [FOLDER] -> Elimina una carpeta
mkdir [FOLDERNAME] -> Crea una carpeta en la ruta actual
rmdir [FOLDERNAME] -> Elimina una carpeta en la ruta actual
sudo -> Brinda permisos de administrador (superusuario)
nano -> Abre un archivo específico
```

Inicialmente se debe configurar la identidad de la cuenta para posteriormente realizar la sincronización del repositorio local con el repositorio web, teniendo en cuenta los siguientes comandos:

```git
git config --global user.name “[USERNAME]” (ej: git config --global user.name “FBarreraP”)
git config --global user.email “[USEREMAIL]” (ej: git config --global user.email “fbarrera6@gmail.com”)
```
Para crear un repositorio web a partir de una carpeta local (PC)

```
Entrar a la carpeta a través del terminal teniendo en cuenta los comandos linux anteriormente presentados
git init 
touch README.md
git add README.md 
git commit -m "algun_comentario" 
git branch -M main
git remote add origin https://github.com/FBarreraP/nombre_repositorio_web.git (ej: https://github.com/FBarreraP/ElectivaRobotica.git)
git push -u origin main 
```

Para crear un repositorio local (PC) desde un repositorio web

```
Entrar a la carpeta a través del terminal teniendo en cuenta los comandos linux anteriormente presentados (No crear carpeta del repositorio, porque se crea automáticamente con los siguientes comandos:)
git clone https://github.com/FBarreraP/nombre_repositorio_web.git (ej: https://github.com/FBarreraP/ElectivaRobotica.git)
cd nombre_repositorio_web (ej: ElectivaRobotica)
```

Para sincronizar los repositorios (web y local) se utilizan los siguientes comandos de git

```
git status
git add --all
git commit -m "algun_comentario"
git push -u origin main
```
Algunas veces que se empujen (<em>push</em>) los archivos del repositorio local al repositorio web desde el terminal por defecto de Raspbian hay que autenticar (usuario y contraseña) el perfil, sin embargo, se debe colocar una <em>Key</em>, siguiendo los siguientes pasos:<br>

https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens

I. <br>
II. <br>
III. <br>

Si se tienen dos repositorios locales (dos computadores), es necesario actualizar el repositorio desactualizado, a través del siguiente comando:

```
git pull origin main
```