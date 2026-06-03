---
search:
  boost: 10.0
---

# Class: AppStore 


_An application or platform for distribution of other applications_



<div data-search-exclude markdown="1">



URI: [tech:AppStore](https://w3id.org/lmodel/dpv/tech/AppStore)





```mermaid
 classDiagram
    class AppStore
    click AppStore href "../AppStore/"
      DpvApplication <|-- AppStore
        click DpvApplication href "../DpvApplication/"
      
      
```





## Inheritance
* [DpvApplication](DpvApplication.md) [ [Software](Software.md)]
    * **AppStore**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:AppStore](https://w3id.org/lmodel/dpv/tech/AppStore) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Application Store




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#AppStore |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:AppStore |
| native | tech:AppStore |
| exact | dpv_tech:AppStore, dpv_tech_owl:AppStore |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AppStore
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#AppStore
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: An application or platform for distribution of other applications
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Application Store
exact_mappings:
- dpv_tech:AppStore
- dpv_tech_owl:AppStore
is_a: DpvApplication
class_uri: tech:AppStore

```
</details>

### Induced

<details>
```yaml
name: AppStore
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#AppStore
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: An application or platform for distribution of other applications
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Application Store
exact_mappings:
- dpv_tech:AppStore
- dpv_tech_owl:AppStore
is_a: DpvApplication
class_uri: tech:AppStore

```
</details></div>