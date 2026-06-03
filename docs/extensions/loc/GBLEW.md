---
search:
  boost: 10.0
---

# Class: GBLEW 


_Concept representing region London Borough of Lewisham in country United_

_Kingdom of Great Britain and Northern Ireland_



<div data-search-exclude markdown="1">



URI: [loc:GB-LEW](https://w3id.org/lmodel/dpv/loc/GB-LEW)





```mermaid
 classDiagram
    class GBLEW
    click GBLEW href "../GBLEW/"
      GB <|-- GBLEW
        click GB href "../GB/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [EEA31](EEA31.md)
        * [GB](GB.md) [ [EU28](EU28.md)]
            * **GBLEW**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GB-LEW](https://w3id.org/lmodel/dpv/loc/GB-LEW) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* GB-LEW
* London Borough of Lewisham




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GB-LEW |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GB-LEW |
| native | loc:GBLEW |
| exact | dpv_loc:GB-LEW, dpv_loc_owl:GB-LEW |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GBLEW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-LEW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Lewisham in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-LEW
- London Borough of Lewisham
exact_mappings:
- dpv_loc:GB-LEW
- dpv_loc_owl:GB-LEW
is_a: GB
class_uri: loc:GB-LEW

```
</details>

### Induced

<details>
```yaml
name: GBLEW
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GB-LEW
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region London Borough of Lewisham in country United

  Kingdom of Great Britain and Northern Ireland'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- GB-LEW
- London Borough of Lewisham
exact_mappings:
- dpv_loc:GB-LEW
- dpv_loc_owl:GB-LEW
is_a: GB
class_uri: loc:GB-LEW

```
</details></div>