import { useState } from "react";
import EntryCard from "./EntryCard";

// filters entries based on whether they're completed or not, value is the boolean for completion
const filterEntries = (arr, value) => {
  const filteredArr = [...arr].filter((entry) => {
    return entry.completed === value;
  });
  return filteredArr;
};

export default function EntryList(props) {
  const [entries, setEntries] = useState(filterEntries(props.entries, false));

  const handleSort = (e) => {
    const sortedEntries = [...entries].sort((a, b) => {
      return a[e.target.value] > b[e.target.value];
    });
    setEntries(sortedEntries);
  };

  const handleFilter = (e) => {
    let filteredEntries = [];
    if (e.target.value === "completed") {
      filteredEntries = filterEntries([...props.entries], true);
    } else if (e.target.value === "incomplete") {
      filteredEntries = filterEntries([...props.entries], false);
    }
    setEntries(filteredEntries);
  };

  return (
    <div className="entry-list">
      <label htmlFor="sort">Sort by:</label>

      <select name="sort" onChange={(e) => handleSort(e)}>
        <option value="" disabled selected>
          Select your option
        </option>
        <option value="xp">XP</option>
        <option value="difficulty">Difficulty</option>
      </select>

      <label htmlFor="filter">Filter by:</label>
      <select name="filter" onChange={(e) => handleFilter(e)}>
        <option value="" disabled selected>
          Select your option
        </option>
        <option value="completed">Complete</option>
        <option value="incomplete">Incomplete</option>
      </select>

      <button className="btn-add-entry" onClick={props.toggleModal}>
        Add Entry
      </button>

      {entries.length > 0
        ? entries.map((entry) => {
            return <EntryCard key={entry.id} entry={entry} />;
          })
        : "You don't have any entries yet :("}
    </div>
  );
}
