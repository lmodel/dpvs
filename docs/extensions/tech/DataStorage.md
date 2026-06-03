---
search:
  boost: 10.0
---

# Class: DataStorage 


_Technology associated with storage of data_



<div data-search-exclude markdown="1">



URI: [tech:DataStorage](https://w3id.org/lmodel/dpv/tech/DataStorage)





```mermaid
 classDiagram
    class DataStorage
    click DataStorage href "../DataStorage/"
      Software <|-- DataStorage
        click Software href "../Software/"
      

      DataStorage <|-- CloudStorage
        click CloudStorage href "../CloudStorage/"
      DataStorage <|-- Database
        click Database href "../Database/"
      DataStorage <|-- LocalStorage
        click LocalStorage href "../LocalStorage/"
      

      
```





## Inheritance
* **DataStorage** [ [Software](Software.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:DataStorage](https://w3id.org/lmodel/dpv/tech/DataStorage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Data Storage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#DataStorage |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:DataStorage |
| native | tech:DataStorage |
| exact | dpv_tech:DataStorage, dpv_tech_owl:DataStorage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataStorage
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#DataStorage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology associated with storage of data
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Data Storage
exact_mappings:
- dpv_tech:DataStorage
- dpv_tech_owl:DataStorage
mixins:
- Software
class_uri: tech:DataStorage

```
</details>

### Induced

<details>
```yaml
name: DataStorage
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#DataStorage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology associated with storage of data
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Data Storage
exact_mappings:
- dpv_tech:DataStorage
- dpv_tech_owl:DataStorage
mixins:
- Software
class_uri: tech:DataStorage

```
</details></div>