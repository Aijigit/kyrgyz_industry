document.querySelectorAll('td.td-title').forEach(td=>{
    td.dataset.content=td.textContent;
    td.textContent=td.textContent.substr(0,20) + '...';
  });
