export default function EntryModal(props) {
  const showModal = props.showModal;

  if (showModal) {
    const entry = props.entry || "";

    // the ternaries in the defaultValues are for editing existing entries
    // prevents it from breaking if we're just creating a new one (no entry in props)
    return (
      <div className="entry-modal">
        <form>
          <label htmlFor="title">Title: </label>
          <input
            type="text"
            name="title"
            defaultValue={entry ? entry.title : null}
          />
          <br />
          <label htmlFor="description">Description: </label>
          <textarea
            placeholder="entry info"
            name="description"
            defaultValue={entry ? entry.description : null}
          />
          <br />
          <label htmlFor="entry-parent">Parent Entry: </label>
          <select name="entry-parent">
            <option value="" disabled selected>
              Select your option
            </option>
            <option value="xp">XP</option>
          </select>
          <br />
          <label htmlFor="entry-type">Entry Type: </label>
          <select name="entry-type">
            <option value="" disabled selected>
              Select your option
            </option>
            <option value="xp">XP</option>
          </select>
          <br />
          <label htmlFor="entry-difficulty">Difficulty: </label>
          <input
            type="number"
            name="entry-difficulty"
            min="1"
            max="10"
            defaultValue={entry ? entry.difficulty : null}
          />{" "}
          <br />
          <label htmlFor="entry-completed">Completed: </label>
          <input
            type="checkbox"
            name="entry-completed"
            value="True"
            defaultChecked={entry ? entry.completed : null}
          />
          <br />
          <input type="hidden" name="user" value={entry ? entry.user : null} />
          <input type="submit" value="Submit" />
        </form>
      </div>
    );
  }
  return null;
}
