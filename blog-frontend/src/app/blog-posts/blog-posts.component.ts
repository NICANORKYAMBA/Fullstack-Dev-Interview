import { Component, OnInit } from '@angular/core';
import { BlogPost } from '../models/blog-post.model';

import { BlogApiService } from '../blog-api.service';


@Component({
  selector: 'blog-posts',
  templateUrl: './blog-posts.component.html',
  styleUrl: './blog-posts.component.css'
})
export class BlogPostsComponent {
  blogPosts: BlogPost[] = [];
  currentPage: number = 1;
  pageSize: number = 10;
  totalPages: number = 0;
  filters: any = {};
  sort: string = '';
  
  constructor(private blogApiService: BlogApiService) { }

  ngOnInit(): void {
	this.getBlogPosts();
  }

  getBlogPosts() {
	this.blogApiService
	  .getBlogPosts(this.currentPage, this.pageSize, this.filters, this.sort)
	  .subscribe((data) => {
		this.blogPosts = data;
		this.totalPages = Math.ceil(data.length / this.pageSize);
	  });
  }

  changePage(page: number) {
	this.currentPage = page;
	this.getBlogPosts();
  }

  changePageSize(size: number) {
	this.pageSize = size;
	this.currentPage = 1;
	this.getBlogPosts();
  }

  changeFilters(filters: any) {
	this.filters = filters;
	this.currentPage = 1;
	this.getBlogPosts();
  }

  changeSort(sort: string) {
	this.sort = sort;
	this.currentPage = 1;
	this.getBlogPosts();
  }
}
