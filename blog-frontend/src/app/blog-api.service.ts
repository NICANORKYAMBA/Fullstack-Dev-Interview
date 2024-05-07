import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';
import { BlogPost } from '../models/blog-post.model';

@Injectable({
  providedIn: 'root'
})
export class BlogApiService {
  private apiUrl = 'http://localhost:8000/api/posts';

  constructor(private http: HttpClient) { }

  getBlogPosts(page?: number, limit? number, filters?: any, sort?: string): Observable<BlogPost[]> {
	  let url = this.apiUrl;
	  let queryParams = [];

	  if (page && limit) {
		  queryParams.push(`page=${page}`);
		  queryParams.push(`limit=${limit}`);
	  }

	  if (filters) {
		  Object.keys(filters).forEach((key) => {
			  queryParams.push(`${key}=${filters[key]}`);
		  });
	  }

	  if (sort) {
		  queryParams.push(`sort=${sort}`);
	  }

	  if (queryParams.length > 0) {
		  url += '?' + queryParams.join('&');
	  }

	  return this.http.get<BlogPost[]>(url);
  }
}
