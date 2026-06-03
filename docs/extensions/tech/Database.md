---
search:
  boost: 10.0
---

# Class: Database 


_A database, database management system (DBMS), or application database_



<div data-search-exclude markdown="1">



URI: [tech:Database](https://w3id.org/lmodel/dpv/tech/Database)





```mermaid
 classDiagram
    class Database
    click Database href "../Database/"
      DataStorage <|-- Database
        click DataStorage href "../DataStorage/"
      
      
```





## Inheritance
* **Database** [ [DataStorage](DataStorage.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Database](https://w3id.org/lmodel/dpv/tech/Database) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Database




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Database |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Database |
| native | tech:Database |
| exact | dpv_tech:Database, dpv_tech_owl:Database |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Database
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Database
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: A database, database management system (DBMS), or application database
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Database
exact_mappings:
- dpv_tech:Database
- dpv_tech_owl:Database
mixins:
- DataStorage
class_uri: tech:Database

```
</details>

### Induced

<details>
```yaml
name: Database
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Database
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: A database, database management system (DBMS), or application database
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Database
exact_mappings:
- dpv_tech:Database
- dpv_tech_owl:Database
mixins:
- DataStorage
class_uri: tech:Database

```
</details></div>