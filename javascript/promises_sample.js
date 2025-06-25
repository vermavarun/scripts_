let promise = new Promise(async (resolve, reject) => {
    await sleep(1000);
    const a = Math.random();
    if ( a < 0.5) {
        resolve(a);
    }
    else {
        reject(a);
    }
});

promise.then((value) => {
    console.log('Resolved: ' + value);
}
).catch((error) => {
    console.log('Rejected: ' + error);
});



function sleep(ms) {
    return new Promise((resolve) => {
      setTimeout(resolve, ms);
    });
  }
