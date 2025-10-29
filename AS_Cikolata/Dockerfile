FROM node:20-alpine

WORKDIR /app

# Копируем package.json и package-lock.json для установки зависимостей
COPY ./package*.json ./
RUN npm install

# Копируем остальные файлы
COPY ./ /app/

# Собираем фронтенд
RUN npm run build

# Используем nginx для работы фронтенда
FROM nginx:alpine
COPY --from=0 /app/dist /usr/share/nginx/html
