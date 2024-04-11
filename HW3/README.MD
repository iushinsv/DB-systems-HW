# Домашняя работа №3. CouchDB + PouchDB.

## 1. Установка CouchBase
### 1.1 На оффициальном [сайте](https://www.couchbase.com/downloads/?family=couchbase-server) скачивем CouchBase-Server:
![](downloading_couchBase_server.png)

### 1.2 выполняем данную команду:
![](unpacking_downloaded_debian_pack.png)
после чего **получаем данный результат** в терминале:
![](unpacking_result.png)

### 1.3 В браузере переходим на http://localhost:8091 и настраиваем наш сервер (создаем кластер):
![](configurating_server.png)

### 1.4 Установка завершена:
![](all_works.png)

## 2. Создание БД в CouchBase
### Создаем my_bucket в my_cluster > Buckets:
![](creating_my_bucket.png)
Что является аналогом базы данных в Р-СУБД

## 3.Добавление документа в БД
Добавим в my_bucket документ с полем **"name"** со значением **"Iushin"**:
![](adding_new_document.png)
Таким образом, действительно, **добавили новый документ**:
![](watching_new_document.png)

## 4.запуск ДЗ3.html
после запуска данного файла и нажатия кнопки sync **ничего не происходило**, т.к. в яндекс браузере(в браузере в котором открывался сам файл) не были выключены [CORS(Cross-origin resource sharing) настройки](https://ru.wikipedia.org/wiki/Cross-origin_resource_sharing) и появлялись **данные ошибки**:
![](CORS_problems.png)
После же отключения CORS, все заработало, и появилась моя фамилия на экране после нажатия кнопки **sync**:
![](it_works.png)

## 5.Остановка Couchbase сервера
выполняем остановку нашего сервера через данную команду:
![](comand_to_stop_couchbase_server.png)
и замечаем, как ui интерфейс сразу сообщает нам об этом:
![](UI_shows_that_server_is_stoped.png)

## 6.Обновление файла ДЗ3.html
Обновляем файл ДЗ3.html и нажимаем кнопку sync, после чего убеждаемся что **моя фамилия по-прежнему на месте!**
![](it_still_works.png)

Файл с синхронизированными в offline данными из CouchDB находится в данной директории.

## Итог
Таким образом, в рамках выполнения данного домашнего задания сделали первое offline-first приложение, взаимодействующее с CouchBase!
