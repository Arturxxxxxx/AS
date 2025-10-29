# Используем образ для React
FROM node:16-alpine AS build

# Установим рабочую директорию
WORKDIR /app



# Копируем package.json и устанавливаем зависимости
COPY AS_Cikolata/package*.json ./
RUN npm install

# Копируем все исходники
COPY ./AS_Cikolata /app/

# Собираем фронтенд
RUN npm run build

# Используем nginx для сервировки статичных файлов
FROM nginx:alpine

# Копируем собранный фронтенд в директорию nginx
COPY --from=build /app/build /usr/share/nginx/html

# Экспонируем порт
EXPOSE 80

# Запускаем nginx
CMD ["nginx", "-g", "daemon off;"]
