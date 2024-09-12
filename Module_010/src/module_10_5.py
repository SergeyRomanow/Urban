# ============================================================================

# Coding            : utf-8

# Script Name	    : Создание потоков
# File              : module_10_*.py

# Author			: Sergey Romanov
# Created			: 01.10.2024
# Last Modified	    : 01.10.2024
# Version			: 1.0.001

# Modifications	:
# Modifications	: 1.0.1 - Tidy up the comments and syntax

# Description       : main script
# Description		: This will go through
#                     and backup all my automator services workflows

# ============================================================================

__author__ = 'Sergey Romanov'
__version__ = '1.0.001'

RSL_DEBUG = True

'''
Практическое задание
2023/12/15 00:00|
Домашнее задание по теме 
"Многопроцессное программирование"
'''

from multiprocessing import Process, Queue


class WarehouseManager :
    """ class WarehouseManager """

    def __init__ ( self ) :
        super ( ).__init__ ( )
        self.data = { }
        self.queue = Queue ( )  # for subprocess communication

    def process_request ( self, request: tuple, data ) :
        """Processing single change request of warehouse inventory data"""
        product, method, amount = request
        self.data = data
        if method == "receipt" :  # in case of adding
            if product in self.data.keys ( ) :  # check if there is already
                # same product, add if not
                self.data [ product ] += amount
            else :
                self.data [ product ] = amount
        elif method == "shipment" :  # in case of removing
            if (product in
                    (self.data.keys ( )) and
                    (self.data [ product ] > 0)
            ) :
                # check if product exists and bigger than 0
                self.data [ product ] -= amount
        else :
            # only two method allowed, otherwise raise exception
            raise Exception ( "Bad request" )
        self.queue.put ( self.data )  # communication between processes

    def run ( self, requests_ ) :
        """Starts individual subprocess for each request"""
        procs = [ ]
        for request_ in requests :
            # we need to pass 'self.data' to each process!!!
            proc = \
                (
                        Process
                                (
                                target = self.process_request,
                                args = (request_, self.data,)
                                )
                )

            proc.start ( )
            procs.append ( proc )

            # communication between processes
            self.data = self.queue.get ( )

            # not really necessary, but still...
        for proc in procs :
            proc.join ( )


if __name__ == "__main__" :
    # initialising manager
    manager = WarehouseManager ( )

    # multiple requests
    requests = [
            ("product1", "receipt", 100),
            ("product2", "receipt", 150),
            ("product1", "shipment", 30),
            ("product3", "receipt", 200),
            ("product2", "shipment", 50)
            ]

    # start processing requests
    manager.run ( requests )

    # displaying updated data on warehouse stocks
    print ( manager.data )
