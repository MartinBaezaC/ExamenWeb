var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
  'aplicacion/inicio' 
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('activate', function(event) {
  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      return Promise.all(
        cacheNames.filter(function(cacheName) {
          // Return true if you want to remove this cache,
          // but remember that caches are shared across
          // the whole origin
          //return true;        
        }).map(function(cacheName) {
          return caches.delete(cacheName);
        })
      );
    })
  );
});

self.addEventListener('fetch', function(event) {
  /*
  event.respondWith(
    new Response("Respuesta con fetch listener")
  );
  
  
  //Respuesta con Notificación PUSH
  /*
  const title = 'Ascensores Web';
  const options = {
    body: 'Bienvenido',
    icon: 'img/ascensor1.png'
  };

  const notificationPromise = self.registration.showNotification(title, options);
  event.waitUntil(notificationPromise);
  */

});

