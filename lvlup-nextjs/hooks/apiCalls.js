import axios from "axios";
import useSWR from "swr";
import { apiURL } from "../Constants.js";

const getUser = async (id) => {
  try {
    const res = await axios.get(`${apiURL}/users/${id}`);
    console.log("i am res", res);
    return res.data;
  } catch (error) {
    console.log(error);
    // throw error;
  }
};

export async function removeEntry(id) {
  try {
    const res = await axios.get(`${apiURL}/entries/${id}`);
    useUser(res.data.user);
  } catch (error) {
    console.log(error);
    // throw error;
  }
}

export async function addEntry(entry) {
  try {
    const res = await axios.post(`${apiURL}/entries`, { entry });
    useUser(res.data.user);
  } catch (error) {
    console.log(error);
    // throw error;
  }
}

export async function editEntry(entry) {
  try {
    const res = await axios.patch(`${apiURL}/entries/${entry.id}`, { entry });
    useUser(res.data.user);
  } catch (error) {
    console.log(error);
    // throw error;
  }
}

export default function useUser(id) {
  console.log("i am once again being called");
  const { data, error, mutate } = useSWR(`${apiURL}/users/${id}`, () =>
    getUser(id)
  );

  return {
    api_user: data,
    isLoading: !error && !data,
    isError: error,
    setUser: mutate,
  };
}
