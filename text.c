/* mm-naive.c - The fastest, least memory-efficient malloc package.
 * In this naive approach, a block is allocated by simply incrementing
 * the brk pointer.  A block is pure payload. There are no headers or
 * footers.  Blocks are never coalesced or reused. Realloc is
 * implemented directly using mm_malloc and mm_free. */
/* NOTE TO STUDENTS: Replace this header comment with your own header
 * comment that gives a high level description of your solution.
 * okok let go */
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <unistd.h>
#include <string.h>

#include "mm.h"
#include "memlib.h"
// team - info
team_t team = {
    // Team name //
    "team 932",
    // First member's full name //
    "jayK",
    // First member's email address //
    "jayK.com",
    // Second member's full name (leave blank if none) //
    "",
    // Second member's email address (leave blank if none) //
    ""};

// global vars//
static char *mem_strt;     // 메모리 시작 주소
static char *mem_brk;      // 메모리 끝 주소 +1
static char *mem_max_addr; // 최대 유효 힙 주소 + 1

// 전처리기 매크로 할당
#define wsize 4                           // 워드는 4바이트
#define dsize 8                           // 더블워드는 8바이트
#define cunksize (1 << 12)                // 청크 하나에 4KB할당(페이지 크기랑 일치해서 편할듯)
#define max(x, y) ((x) > (y) ? (x) : (y)) // x,y중 max값

// 크기와 가용여부를 합쳐서(비트연산 활용) 표시함
#define pack(size, alloc) ((size) | (alloc)) // or연산으로 헤더에서 쓸 word만들어줌

// 주소p에 r/w
#define get(p) (*(unsigned int *)(p))                     // 포인터로 주소p를 참조, 블록 이동할 때 쓸거
#define put(p, val) (*(unsigned int *)(p)) = ((int)(val)) // 주소 p에 val이라는 주소를 담음

// 주소p에서 크기와 할당여부를 읽어옴
#define get_size(p) (get(p) & ~0x7) // &와 ~를 이용해 뒷 3자리를 제외한 비트를 가져옴
#define get_alloc(p) (get(p) & 0x1) // 0번째 비트(할당여부)를 가져옴

//(char*)인 이유는 1바이트 단위로 조작이 가능해서임
#define header_of(bp) ((char *)(bp)-wsize)                           // header 포인터
#define footer_of(bp) ((char *)(bp) + get_size(hdrp(bp)) - dsize)    // FooTer 포인터, 항상 header에 넣은 양을 씀
#define next_block(bp) ((char *)(bp) + get_size((char *)(bp)-wsize)) // 다음블럭으로 ㄱㄱ
#define prev_block(bp) ((char *)(bp)-get_size((char *)(bp)-dsize))   // 이전블록으로 ㄲㄲ

static char *heap_listp; // heap init해줌 (4KB)

// single word (4) or double word (8) alignment //
#define ALIGNMENT 8

// rounds up to the nearest multiple of ALIGNMENT //
#define ALIGN(size) (((size) + (ALIGNMENT - 1)) & ~0x7)

#define SIZE_T_SIZE (ALIGN(sizeof(size_t)))
//
#define chunksize (1 << 12)
//
// mm_init - initialize the malloc package.
//
int mm_init(void)
{
    if ((heap_listp = mem_sbrk(4 * wsize)) == (void *)-1)
    {
        return -1;
    }
    put(heap_listp, 0);//블록 생성할때 
    put(heap_listp + (1 * wsize), pack(dsize, 1));
    put(heap_listp + (2 * wsize), pack(dsize, 1));
    put(heap_listp + (3 * wsize), pack(dsize, 1));
    heap_listp += (2 * wsize);

    return 0;
}

//
// mm_malloc - Allocate a block by incrementing the brk pointer.
// Always allocate a block whose size is a multiple of the alignment.
//
void *mm_malloc(size_t size)
{
    int newsize = ALIGN(size + SIZE_T_SIZE);
    void *p = mem_sbrk(newsize);
    if (p == (void *)-1)
        return NULL;
    else
    {
        *(size_t *)p = size;
        return (void *)((char *)p + SIZE_T_SIZE);
    }
}

//
// mm_free - Freeing a block does nothing.
//
void mm_free(void *ptr)
{
}

//
// mm_realloc - Implemented simply in terms of mm_malloc and mm_free
//
void *mm_realloc(void *ptr, size_t size)
{
    void *oldptr = ptr;
    void *newptr;
    size_t copySize;

    newptr = mm_malloc(size);
    if (newptr == NULL)
        return NULL;
    copySize = *(size_t *)((char *)oldptr - SIZE_T_SIZE);
    if (size < copySize)
        copySize = size;
    memcpy(newptr, oldptr, copySize);
    mm_free(oldptr);
    return newptr;
}
