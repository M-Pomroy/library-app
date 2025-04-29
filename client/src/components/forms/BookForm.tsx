import { FormEvent, useState } from "react";
import { useFormik } from "formik";
import * as Yup from "yup";
import axios from "../../axios";
import "../../styles/form.css";
import { Book } from "../../types";

const BookForm = () => {
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const handleSubmit = async () => {
    console.log("submitting");
    setIsLoading(true);

    const newBook: Book = {
      title: formik.values.title,
      author: formik.values.author,
      format: formik.values.format_id,
      releaseDate: formik.values.release_date,
      isbn: formik.values.isbn,
      description: formik.values.book_description,
    };

    try {
      const response = await axios.post<{ message: String; book: Book }>(
        "/api/addBook",
        newBook
      );
      console.log("Book added successfully", response.data.book);
    } catch (error) {
      console.log("Error adding book:", error);
    } finally {
      setIsLoading(false);
    }
  };

  const formik = useFormik({
    initialValues: {
      title: "",
      author: "",
      book_description: "",
      release_date: "",
      isbn: "",
      format_id: "",
    },
    onSubmit: handleSubmit,
    validationSchema: Yup.object({
      title: Yup.string().required("Please enter a title"),
      author: Yup.string().required("Please enter an author"),
      book_description: Yup.string().notRequired(),
      release_date: Yup.date().notRequired(),
      isbn: Yup.string().notRequired(),
      format_id: Yup.string().required("Please select a format"),
    }),
  });

  return (
    <div className="section">
      <div className="container container-960">
        <form className="form" onSubmit={formik.handleSubmit}>
          <div className="field">
            <label htmlFor="title" className="field-label">
              Title*
            </label>
            {formik.touched.title && formik.errors.title ? (
              <p className="field-error">{formik.errors.title}</p>
            ) : null}
            <input
              type="text"
              id="title"
              name="title"
              value={formik.values.title}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              className="field-input"
              required
            />
          </div>

          <div className="field">
            <label htmlFor="author" className="field-label">
              Author*
            </label>
            {formik.touched.author && formik.errors.author ? (
              <p className="field-error">{formik.errors.author}</p>
            ) : null}
            <input
              type="text"
              id="author"
              name="author"
              value={formik.values.author}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              className="field-input"
              required
            />
          </div>

          <div className="field-group">
            <div className="field">
              <label htmlFor="format_id" className="field-label">
                Format*
              </label>
              {formik.touched.format_id && formik.errors.format_id ? (
                <p className="field-error">{formik.errors.format_id}</p>
              ) : null}
              <select
                id="format_id"
                name="format_id"
                value={formik.values.format_id}
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                className="field-input"
                required
              >
                <option value="">Please select a format</option>
                <option value="0">Paperback</option>
                <option value="1">Hardback</option>
                <option value="2">EBook</option>
              </select>
            </div>

            <div className="field">
              <label htmlFor="release_date" className="field-label">
                Release Date
              </label>
              <input
                type="date"
                id="release_date"
                name="release_date"
                value={formik.values.release_date}
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                className="field-input"
              />
            </div>

            <div className="field">
              <label htmlFor="isbn" className="field-label">
                ISBN
              </label>
              <input
                type="text"
                id="isbn"
                name="isbn"
                value={formik.values.isbn}
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                className="field-input"
              />
            </div>
          </div>

          <div className="field">
            <label htmlFor="book_description" className="field-label">
              Description
            </label>
            <textarea
              id="book_description"
              name="book_description"
              value={formik.values.book_description}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              className="field-textarea"
            ></textarea>
          </div>

          <button type="submit" className="form-submit">
            Submit
          </button>
        </form>
      </div>
    </div>
  );
};

export default BookForm;
