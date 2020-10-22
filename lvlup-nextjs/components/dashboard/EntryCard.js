export default function EntryCard(props) {
  return (
    <div className="entry-card">
      {props.entry ? (
        <div className="container">
          <h4>
            <b>{props.entry.name}</b>
            <button className="btn-edit-entry">Edit</button>
            <button className="btn-delete-entry">Delete</button>
          </h4>
          <p>{props.entry.description}</p>
          <label htmlFor="entry-checkbox"></label>
          <input
            type="checkbox"
            className="entry-checkbox"
            defaultChecked={props.entry.completed}
          ></input>
          <p>Difficulty: {props.entry.difficulty}</p>
          <p>XP: {props.entry.xp}</p>
        </div>
      ) : (
        "We ran into a problem with this entry :("
      )}
    </div>
  );
}
