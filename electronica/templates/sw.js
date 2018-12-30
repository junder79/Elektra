;
//asignar un nombre y versión al cache
const CACHE_NAME = 'ELEKTRAPWA',
  urlsToCache = [
    './',
    './tiendas',
    './productos',
    './ventas',
    './productitos',

  ]

//durante la fase de instalación, generalmente se almacena en caché los activos estáticos
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache)
          .then(() => self.skipWaiting())
      })
      .catch(err => console.log('Falló registro de cache', err))
  )
})

//una vez que se instala el SW, se activa y busca los recursos para hacer que funcione sin conexión
self.addEventListener('activate', e => {
  const cacheWhitelist = [CACHE_NAME]

  e.waitUntil(
    caches.keys()
      .then(cacheNames => {
        return Promise.all(
          cacheNames.map(cacheName => {
            //Eliminamos lo que ya no se necesita en cache
            if (cacheWhitelist.indexOf(cacheName) === -1) {
              return caches.delete(cacheName)
            }
          })
        )
      })
      // Le indica al SW activar el cache actual
      .then(() => self.clients.claim())
  )
})

//cuando el navegador recupera una url
self.addEventListener('fetch', e => {
  //Responder ya sea con el objeto en caché o continuar y buscar la url real
  e.respondWith(
    caches.match(e.request)
      .then(res => {
        if (res) {
          //recuperar del cache
          return res
        }
        //recuperar de la petición a la url
        return fetch(e.request)
      })
  )
})

//Notificaciones PUSH

self.addEventListener('push', e => {
  console.log('Evento: Push')

  let title = 'Push Notificación Demo',
    options = {
      body: 'Click para regresar a la aplicación',
      icon: './img/icon_192x192.png',
      vibrate: [100, 50, 100],
      data: { id: 1 },
      actions: [
        { 'action': 'Si', 'title': 'Amo esta aplicación :)', icon: './img/icon_192x192.png' },
        { 'action': 'No', 'title': 'No me gusta esta aplicación :(', icon: './img/icon_192x192.png' }
      ]
    }

    e.waitUntil( self.registration.showNotification(title, options) )
})