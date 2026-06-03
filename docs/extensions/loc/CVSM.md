---
search:
  boost: 10.0
---

# Class: CVSM 


_Concept representing region São Miguel (Cape Verde) in country Cabo_

_Verde_



<div data-search-exclude markdown="1">



URI: [loc:CV-SM](https://w3id.org/lmodel/dpv/loc/CV-SM)





```mermaid
 classDiagram
    class CVSM
    click CVSM href "../CVSM/"
      CV <|-- CVSM
        click CV href "../CV/"
      
      
```





## Inheritance
* [CV](CV.md)
    * **CVSM**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:CV-SM](https://w3id.org/lmodel/dpv/loc/CV-SM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* CV-SM
* São Miguel (Cape Verde)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#CV-SM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:CV-SM |
| native | loc:CVSM |
| exact | dpv_loc:CV-SM, dpv_loc_owl:CV-SM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CVSM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CV-SM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region São Miguel (Cape Verde) in country Cabo

  Verde'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CV-SM
- São Miguel (Cape Verde)
exact_mappings:
- dpv_loc:CV-SM
- dpv_loc_owl:CV-SM
is_a: CV
class_uri: loc:CV-SM

```
</details>

### Induced

<details>
```yaml
name: CVSM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CV-SM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: 'Concept representing region São Miguel (Cape Verde) in country Cabo

  Verde'
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CV-SM
- São Miguel (Cape Verde)
exact_mappings:
- dpv_loc:CV-SM
- dpv_loc_owl:CV-SM
is_a: CV
class_uri: loc:CV-SM

```
</details></div>