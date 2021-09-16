mappings = platsannons_mappings = {
    "mappings": {
        "properties": {
            "id": {
                "type": "keyword"
            },
            "name": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword"
                    }
                }
            },
            "department": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "keyword"
                    },
                    "name": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword"
                            }
                        }
                    },
                    "atHome": {
                        "type": "boolean"
                    }
                }
            },
            "price": {
                "type": "long"
            },
            "preferences": {
                "type": "object",
                "properties": {
                    "dietary": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                }
                            },
                        }
                    },
                    "labels": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                }
                            }
                        }
                    }
                }
            },
        }
    }
}
