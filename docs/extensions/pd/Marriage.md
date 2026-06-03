---
search:
  boost: 10.0
---

# Class: Marriage 


_Information about marriage(s)_



<div data-search-exclude markdown="1">



URI: [pd:Marriage](https://w3id.org/lmodel/dpv/pd/Marriage)





```mermaid
 classDiagram
    class Marriage
    click Marriage href "../Marriage/"
      FamilyStructure <|-- Marriage
        click FamilyStructure href "../FamilyStructure/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Family](Family.md)
        * [FamilyStructure](FamilyStructure.md)
            * **Marriage**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Marriage](https://w3id.org/lmodel/dpv/pd/Marriage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Marriage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Marriage |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Marriage |
| native | pd:Marriage |
| exact | dpv_pd:Marriage, dpv_pd_owl:Marriage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Marriage
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Marriage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about marriage(s)
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Marriage
exact_mappings:
- dpv_pd:Marriage
- dpv_pd_owl:Marriage
is_a: FamilyStructure
class_uri: pd:Marriage

```
</details>

### Induced

<details>
```yaml
name: Marriage
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Marriage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about marriage(s)
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Marriage
exact_mappings:
- dpv_pd:Marriage
- dpv_pd_owl:Marriage
is_a: FamilyStructure
class_uri: pd:Marriage

```
</details></div>