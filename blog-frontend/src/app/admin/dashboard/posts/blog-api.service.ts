import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { BlogPost } from './blog-post.model';

@Injectable({
  providedIn: 'root'
})
export class BlogApiService {
  private apiUrl = 'http://localhost:8000/api/posts/';

  constructor(private http: HttpClient) { }

  getBlogPosts(page: number = 1, limit: number = 10, filters?: any, sort?: string): Observable<BlogPost[]> {
    let params = new HttpParams()
      .set('page', page.toString())
      .set('limit', limit.toString());

    if (filters) {
      Object.keys(filters).forEach((key) => {
        params = params.set(key, filters[key]);
      });
    }

    if (sort) {
      params = params.set('sort', sort);
    }

    return this.http.get<BlogPost[]>(this.apiUrl, { params });
  }
}
