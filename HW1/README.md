# Как я выполнял ДЗ 1

# 1. Установил Docker
Со времен 2го курса у меня на ubuntu уже **было установлено ПО** для работы с докером


<table>
  <tr>
    <td><img src="/pictures/my_docker_Images.png" alt="Image 1"></td>
    <td><img src="/pictures/my_docker_containers.png" alt="Image 2"></td>
  </tr>
</table>

![](/pictures/docker_version.png)
![](/pictures/my_docker_version.png)

Тогда оно было нужно для развертывания Р-СУБД PostgreSQL в рамках курса "Базы данных". Но тогда, честно говоря, упор курса был на изучение самого языка SQL, поэтому устройство докера, его предназначение, механизм работы - все это проходилось поверхностно и больше было каким-то порядком действий, который нужно сделать через терминал на ubuntu по написанной для нас инструкции.
Поэтому прочитанная на нашем курсе "Системы баз данных" лекция про докер была для меня действительно новым и очень интересным материалом, который дал некоторое понимание отличие идеи докера от идеи виртуальных машин.
Но, так как в этом курсе начинается уже серъезная работа связанная с докером, мне захотело также освоить некоторые практические команды: docker pull/build/...; docker-compose -..;
И в этом **мне помог обучающий основам докера [плейлист](https://youtube.com/playlist?list=PLy7NrYWoggjzfAHlUusx2wuDwfCrmJYcs&si=vIfzree_UXTWC0SJ)**, в котором автор показывает как использовать основные команды докера, как создавать образы и контейнеры, как писать файлы Dockefile и Docker compose



# 2. Установил монгу и запустил ее в виде контейнера
Сделал **pull** основных образов:
![Image alt text](/pictures/docker_pull_mongo.png "pull образа mongo")
![Image alt text](/pictures/docker_pull_mongo-express.png "pull образа mongo-express")

Написал такой **yml** файл для запуска базы данных через docker-compose:
![Image alt text](/pictures/yml_of_mongodb_for_docker-compose_command.png "yml")

**Развернул** базу данных
![Image alt text](/pictures/deploy_mongodb_via_docker-compose.png "deploy")

Подлкючился к ней **используя Compass** через данную ссылку
![Image alt text](/pictures/url_for_connecting_to_hw1_mongodb_via_Compass.png "url")

И как видно, **все исправно работает**
![Image alt text](/pictures/hw1_mongo_is_deployed.png "deployed")


# 3. Закачал датасет
**выбрал** [датасет](https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/problem12.html) №9 из [статьи](https://habr.com/ru/companies/edison/articles/480408/) на habr

![Image alt text](/pictures/9_Titanic_Dataset_from_habr.png )
![Alt text](/pictures/titanic_Dataset.png)

Создал новую базу данных **titanic_db** и коллекцию **titanic_passengers** в ней, куда импортировал выбранный датасет
![Alt text](/pictures/titanic_passengers_imported_in_new_collection.png)


# 4. Выполнил операции CRUD.
## 4.1 Create
Добавим пассажира на наш Титаник с помощью команды **insertOne**
![](/pictures/insert_of_new_passenger.png)

## 4.2 Read
Найдем информацию о новом пассажире в таблице с помощью команды **find**
![](/pictures/find_new_passenger's_info.png)

## 4.3 Replace
Обновим информацию о добавленном пассажире с помощью команды **updateOne**
![](/pictures/update_new_passenger's_info.png)
Проверим, что информация обновилась:
![](/pictures/check_of_update.png)
Да, действительно, поле Pclass обновилось.

## 4.4 Delete
Удалим нашего нового пассажира с Титаника используя команду **delete**
![](/pictures/delete_new_passenger_from_titanic.png)

# 5. Несколько запросов на выборку
Найдем имена выживших пассажиров на нашем титанике в возрасте 24 лет имеющих билет 1го класса:
![](/pictures/query_N_1.png)

Сделаем несколько количественных запросов:
![](/pictures/queries_of_percentages.png)
исходя из которых можно сделать вывод, что среди пассажиров в возрастной группе от 20 до 30 процент выживания был ниже, чем у пассажиров в возрастной группе от 10 до 20 - 33.4% против 37.5

# 6. Об индексах
К сожалению, данный датасет оказался достаточно небольшим, чтобы почувствовать хоть какую-то разницу в скорости поиска тех или иных документов, т.к. даже без создания индексов в базе данных запросы выполнялись за **очень** маленькое время:
например **время выполнения** данного запроса
![](/pictures/find_req.png)
составило значение очень **близкое к 0**, несмотря на то, что запрос **завершился успешно**
![](/pictures/find_req_stat.png)

Поэтому я решил выполнить эту часть домашнего задания на другом [датасете](https://www.kaggle.com/datasets/fivethirtyeight/uber-pickups-in-new-york-city?resource=download)
![](/pictures/new_dataset.png)
где каждый документ имеет **слудующие поля**:
![](/pictures/fields_of_new_dataset.png)
И подобных документов **около 2 миллионов** было добавлено в мою новую коллекцию, что дало ощутимую разницу во времени выполнения find-запросов:
например время выполнения данного запроса заняло уже **2124 ms**:
![](/pictures/fing_req_for_new_dataset.png)
![](/pictures/find_req_for_new_dataset_stat.png)

Теперь в данной коллекции **создадим индекс по атрибуту "Affiliated_base_num"**:
![](/pictures/created_new_ind.png)

и сравним производительность предыдущего find-запроса в новых условиях:
![](/pictures/find_req_with_ind.png)
Время выполнения данного запроса заняло **452 ms**,
![](/pictures/find_req_with_ind_stat.png)
что примерно в **4,7 раза быстрее**, чем без индекса.

# 7. Вывод
### 7.1) В ходе выполнения ДЗ1 я развернул MOngoDB в Docker
### 7.2) Создал базу данных и заполнил её данными из двух датасетов ([titanic](https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/problem12.html), [Uber](https://www.kaggle.com/datasets/fivethirtyeight/uber-pickups-in-new-york-city?resource=download))
### 7.3) Написал несколько CRUD запросов
### 7.4) Создал индекс и сравнил производительность find-запросов и показал, что при поиску по полю, у которого существует индекс, время выполнение запроса в несколько раз уменьшается, что хорошо сказывается на производительности