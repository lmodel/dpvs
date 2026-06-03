---
search:
  boost: 10.0
---

# Class: Interest 


_Information about interests_



<div data-search-exclude markdown="1">



URI: [pd:Interest](https://w3id.org/lmodel/dpv/pd/Interest)





```mermaid
 classDiagram
    class Interest
    click Interest href "../Interest/"
      Preference <|-- Interest
        click Preference href "../Preference/"
      

      Interest <|-- Dislike
        click Dislike href "../Dislike/"
      Interest <|-- Like
        click Like href "../Like/"
      

      
```





## Inheritance
* [Internal](Internal.md)
    * [Preference](Preference.md)
        * **Interest**
            * [Dislike](Dislike.md)
            * [Like](Like.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Interest](https://w3id.org/lmodel/dpv/pd/Interest) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Interest




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Interest |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Interest |
| native | pd:Interest |
| exact | dpv_pd:Interest, dpv_pd_owl:Interest |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Interest
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Interest
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about interests
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Interest
exact_mappings:
- dpv_pd:Interest
- dpv_pd_owl:Interest
is_a: Preference
class_uri: pd:Interest

```
</details>

### Induced

<details>
```yaml
name: Interest
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Interest
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about interests
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Interest
exact_mappings:
- dpv_pd:Interest
- dpv_pd_owl:Interest
is_a: Preference
class_uri: pd:Interest

```
</details></div>