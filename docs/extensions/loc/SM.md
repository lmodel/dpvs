---
search:
  boost: 10.0
---

# Class: SM 


_Concept representing Country of San Marino_



<div data-search-exclude markdown="1">



URI: [loc:SM](https://w3id.org/lmodel/dpv/loc/SM)





```mermaid
 classDiagram
    class SM
    click SM href "../SM/"
      SM <|-- SM01
        click SM01 href "../SM01/"
      SM <|-- SM02
        click SM02 href "../SM02/"
      SM <|-- SM03
        click SM03 href "../SM03/"
      SM <|-- SM04
        click SM04 href "../SM04/"
      SM <|-- SM05
        click SM05 href "../SM05/"
      SM <|-- SM06
        click SM06 href "../SM06/"
      SM <|-- SM07
        click SM07 href "../SM07/"
      SM <|-- SM08
        click SM08 href "../SM08/"
      SM <|-- SM09
        click SM09 href "../SM09/"
      
      
```





## Inheritance
* **SM**
    * [SM01](SM01.md)
    * [SM02](SM02.md)
    * [SM03](SM03.md)
    * [SM04](SM04.md)
    * [SM05](SM05.md)
    * [SM06](SM06.md)
    * [SM07](SM07.md)
    * [SM08](SM08.md)
    * [SM09](SM09.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SM](https://w3id.org/lmodel/dpv/loc/SM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* San Marino




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SM |
| native | loc:SM |
| exact | dpv_loc:SM, dpv_loc_owl:SM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of San Marino
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- San Marino
exact_mappings:
- dpv_loc:SM
- dpv_loc_owl:SM
class_uri: loc:SM

```
</details>

### Induced

<details>
```yaml
name: SM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of San Marino
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- San Marino
exact_mappings:
- dpv_loc:SM
- dpv_loc_owl:SM
class_uri: loc:SM

```
</details></div>