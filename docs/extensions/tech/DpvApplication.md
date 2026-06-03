---
search:
  boost: 10.0
---

# Class: DpvApplication 


_Application or Application Software_



<div data-search-exclude markdown="1">



URI: [tech:Application](https://w3id.org/lmodel/dpv/tech/Application)





```mermaid
 classDiagram
    class DpvApplication
    click DpvApplication href "../DpvApplication/"
      Software <|-- DpvApplication
        click Software href "../Software/"
      

      DpvApplication <|-- AppStore
        click AppStore href "../AppStore/"
      DpvApplication <|-- SmartphoneApplication
        click SmartphoneApplication href "../SmartphoneApplication/"
      

      
```





## Inheritance
* **DpvApplication** [ [Software](Software.md)]
    * [AppStore](AppStore.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Application](https://w3id.org/lmodel/dpv/tech/Application) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Application




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Application |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Application |
| native | tech:DpvApplication |
| exact | dpv_tech:Application, dpv_tech_owl:Application |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DpvApplication
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Application
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Application or Application Software
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Application
exact_mappings:
- dpv_tech:Application
- dpv_tech_owl:Application
mixins:
- Software
class_uri: tech:Application

```
</details>

### Induced

<details>
```yaml
name: DpvApplication
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Application
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Application or Application Software
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Application
exact_mappings:
- dpv_tech:Application
- dpv_tech_owl:Application
mixins:
- Software
class_uri: tech:Application

```
</details></div>