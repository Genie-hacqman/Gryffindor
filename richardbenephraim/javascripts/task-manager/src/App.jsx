import TaskList from "./components/TaskList";



function App(){
  const name = 'Dashlane';
  
  return (
    <div>
      <h1>task manager</h1> 
      <p>this is a task manager {name}</p>
      <p>{45 > 5 ? 'yes its u' : 'no'}</p>
      {/* <TaskList /> */}
    </div>
  )
}


export default App