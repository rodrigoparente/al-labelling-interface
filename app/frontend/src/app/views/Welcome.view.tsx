import LoggedIn from "../layouts/LoggedIn";

export default function WelcomeView() {
  return (
    <LoggedIn>
    <div className="flex justify-center h-screen items-center bg-slate-100" >
      <form className="p-2 border rounded-lg h-56 shadow-md w-72 py-6 flex flex-col gap-4 bg-white" onSubmit={onSubmit}>
        <h1>Welcome</h1>
        <p>This questionary was made for testers to train an learning algorithm.</p>
        <p>Just follow the steps and answer carefully</p>
      </form>
    </div>
    </LoggedIn>
  );
}